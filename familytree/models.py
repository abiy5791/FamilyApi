from django.db import models


class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    birthdate = models.DateField()
    phone_number = models.CharField(max_length=15, blank=True, null=True,)
    married = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True,)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.name


class Relationship(models.Model):
    parent = models.ForeignKey(
        FamilyMember, related_name='children', on_delete=models.CASCADE)
    child = models.ForeignKey(
        FamilyMember, related_name='parents', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.parent.name} -> {self.child.name}"
