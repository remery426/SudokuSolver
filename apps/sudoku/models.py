from __future__ import unicode_literals

from django.db import models

class squareManager(models.Manager):
    def changeval(self,postData):
        response = {}
        errors = []
        if len(postData['new_val'])<1:
            errors.append("Board update failed. Please enter a value!")
        if len(postData['new_val'])>1:
            errors.append("Board update failed. Value must be between 1- 9")
        if len(postData['new_val'])==1:
            try:
                int(postData['new_val'])

            except ValueError:
                errors.append("Value must be an integer!")
        if errors:
            response['status']=False
            response['error']=errors
            return response
        response['status']= True
        return response


class Square(models.Model):
    value = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = squareManager()
