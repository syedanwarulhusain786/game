from django.db import models



class GameData(models.Model):
    ip = models.CharField(max_length=15)
    username = models.CharField(max_length=15,null=True)
    
    lastgame = models.FloatField(null=True,default=0.0)
    current_score = models.FloatField(null=True,default=0.0)
    
    
    def __str__(self):
        return f"IP: {self.ip}, Last Game: {self.lastgame}, Current Score: {self.current_score}"
