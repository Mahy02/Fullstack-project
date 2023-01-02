from django.utils import timezone
from django.db.models import Q
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User   #user table
import string

from django.forms import ValidationError
# Create your models here.

#tables we will need:: team, referee, match, stadium, tickets 

class Teams(models.Model):  #we only have name=> 2 teams only
    name= models.CharField(max_length=30)
    def __str__(self):
       return f'{self.name} '


class Referees(models.Model):  #we only have name =>one referee, 2 linesmen
    name= models.CharField(max_length=30)
    def __str__(self):
        return f'{self.name} '



class Stadiums(models.Model):  #we have name, row and seats
    # idS=models.IntegerField( primary_key=True)
    name=models.CharField(max_length=30)
    seats=models.IntegerField()
    rows=models.IntegerField()
    
    def __str__(self):
        return f'{self.name} '
    def clean(self):
        if self.seats>20 or self.rows>20:
            raise ValidationError("Number of seats or rows shouldn't exceed 20")
        if self.seats<=0 or self.rows<=0:
            raise ValidationError("Number of seats or rows shouldn't be smaller than or equal 0")
    def save(self, *args, **kwargs):
        super(Stadiums, self).save(*args, **kwargs)
        Seats.objects.filter(venue=self).delete()
        
        for row in range(1, self.rows+1):
            for col in range (1, self.seats+1):
                Seats.objects.create(venue=self, row=row, column=col)
           
        super(Stadiums, self).save(*args, **kwargs)

class Seats(models.Model):
    venue=models.ForeignKey(Stadiums, on_delete=models.CASCADE, related_name='seat_venue',null=True)
    row=models.IntegerField()
    column=models.IntegerField()
    # seat_no=models.IntegerField()
    @property
    def seatName(self):
        return f'{string.ascii_uppercase[self.row-1]}{[self.column-1]} '



class Matches(models.Model):  #match has teams(2), referee, 2 linesmen, data and time, venue, score
    #each match has 2 teams so team 1 is one to oen relation
    #matches has their own id
    team_1=models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='team_1') 
    team_2=models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='team_2')
    referee=models.ForeignKey(Referees, on_delete=models.CASCADE, related_name='referee')
    linesman_1=models.ForeignKey(Referees, on_delete=models.CASCADE, related_name='linesman_1')
    linesman_2=models.ForeignKey(Referees, on_delete=models.CASCADE, related_name='linesman_2')
    venue=models.ForeignKey(Stadiums, on_delete=models.CASCADE, related_name='venue')
    date_and_time=models.DateTimeField()
    
    def clean(self):
 
        if self.referee==self.linesman_1 or self.referee==self.linesman_2 or self.linesman_1==self.linesman_2:
            raise ValidationError("A referee should have one role only")
        if self.team_1==self.team_2:
            raise ValidationError("Teams should be unique")
        if self.date_and_time.date()< timezone.now().date():
            raise ValidationError("Please set a date in the future")
        first=Matches.objects.filter(Q(team_1=self.team_1) | Q(team_2=self.team_1))            
        second=Matches.objects.filter(Q(team_1=self.team_2) | Q(team_2=self.team_2)) 
        for m in first:
            if m.date_and_time.date()==self.date_and_time.date():
                raise ValidationError( f"{self.team_1} team is already playing on this day")
        for m in second:
            if m.date_and_time.date()==self.date_and_time.date():
                raise ValidationError(f"{self.team_2}team is already playing on this day")
        venues=Matches.objects.filter(Q(venue=self.venue))     
        for m in venues:
            if m.date_and_time.date()==self.date_and_time.date() and m.date_and_time+timedelta(hours=3)>self.date_and_time:
                raise ValidationError(f"Venue is already booked, should be rebooked after 3 hours from {m.date_and_time.time()}") 
        refr=Matches.objects.filter(Q(referee=self.referee) | Q(linesman_1=self.referee) | Q(linesman_2=self.referee))
        lines1=Matches.objects.filter(Q(referee=self.linesman_1) | Q(linesman_1=self.linesman_1) | Q(linesman_2=self.linesman_1))
        lines2=Matches.objects.filter(Q(referee=self.linesman_2) | Q(linesman_1=self.linesman_2) | Q(linesman_2=self.linesman_2))
        for m in refr:
            if m.date_and_time.date()==self.date_and_time.date():
                raise ValidationError(f"{self.referee} Referee have another match on this day")
        for m in lines1:
            if m.date_and_time.date()==self.date_and_time.date():
                raise ValidationError(f" {self.linesman_1} Linesman have another match on this day")
        for m in lines2:
            if m.date_and_time.date()==self.date_and_time.date():
                raise ValidationError(f" {self.linesman_2} Linesman have another match on this day")
        
    def save(self,*args,**kwargs):
        if self.team_1 is None:
            raise ValidationError ("missing")
        self.full_clean()
        super().save(*args,**kwargs)
    def __str__(self):
        return f'{self.date_and_time} '

class Tickets(models.Model):   #unique ticket number for each user => one user can have more than one ticket number, if user is deleted ticket is deleted
    
    match = models.ForeignKey(Matches, related_name="tickets", null=True, on_delete=models.CASCADE) #each match has many tickets but one ticket for one match
    ticket_seat= models.ForeignKey(Seats, on_delete=models.CASCADE, null=True)  #user can buy many tickets  but one ticeket is for one user =>one to many
    ticket_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="ticket_user",null=True)
    def __str__(self):
        return f'{self.ticket_seat} '
    def clean(self):
        tickets= Tickets.objects.filter(match=self.match)
        for tick in tickets:
            if tick.ticket_seat== self.ticket_seat:
                raise ValidationError(f'seat <{self.ticket_seat}> is already booked ')
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
       
    
    




