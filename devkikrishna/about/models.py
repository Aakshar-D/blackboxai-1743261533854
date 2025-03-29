from django.db import models

class RoomBooking(models.Model):
    ROOM_TYPES = (
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('suite', 'Suite'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('cancelled', 'Cancelled')
        ],
        default='pending'
    )

    def __str__(self):
        return f"Booking by {self.name} - {self.check_in} to {self.check_out}"

    class Meta:
        ordering = ['-booking_date']