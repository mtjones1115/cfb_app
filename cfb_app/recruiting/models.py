from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone


# Create your models here.

class Player(models.Model):
    class Position(models.TextChoices):
        ATH = 'ATH', 'Athlete'
        QB = 'QB', 'Quarterback'
        HB = 'HB', 'Halfback'
        FB = 'FB', 'Fullback'
        TE = 'TE', 'Tight End'
        WR = 'WR', 'Wide Receiver'
        OT = 'OT', 'Offensive Tackle'
        OG = 'OG', 'Offensive Guard'
        DT = 'DT', 'Defensive Tackle'
        DE = 'DE', 'Defensive End'
        MLB = 'MLB', 'Middle Linebacker'
        OLB = 'OLB', 'Outside Linebacker'
        CB = 'CB', 'Cornerback'
        FS = 'FS', 'Free Safety'
        SS = 'SS', 'Strong Safety'
        P = 'P', 'Punter'
        K = 'K', 'Kicker'

    class Year(models.TextChoices):
        FR = 'FR', 'Freshman'
        RS_FR = 'FR(RS)', 'Freshman (Redshirt)'
        SO = 'SO', 'Sophomore'
        RS_SO = 'SO(RS)', 'Sophomore (Redshirt)'
        JR = 'JR', 'Junior'
        RS_JR = 'JR(RS)', 'Junior (Redshirt)'
        SR = 'SR', 'Senior'
        RS_SR = 'SR(RS)', 'Senior (Redshirt)'

    class Dev(models.TextChoices):
        NRM = 'Nrm', 'Normal'
        IMP = 'IMP', 'Impact'
        STR = 'STR', 'Star'
        ELT = 'ELT', 'Elite'

    class Eligibility(models.TextChoices):
        REC = 'REC', 'Recruit'
        ENR = 'ENR', 'Enrolled'
        GRD = 'GRD', 'Graduated'

    class Interests(models.TextChoices):
        PT = 'PT', 'Playing Time'
        PS = 'PS', 'Playing Style'
        CC = 'CC', 'Championship Contender'
        TR = 'TR', 'Program Tradition'
        CL = 'CL', 'Campus Lifestyle'
        SA = 'SA', 'Stadium Atmosphere'
        PP = 'PP', 'Pro Potential'
        BE = 'BE', 'Brand Exposure'
        AP = 'AP', 'Academic Prestige'
        CP = 'CP', 'Conference Prestige'
        CO = 'CO', 'Coach Prestige'
        CS = 'CS', 'Coach Stability'
        AF = 'AF', 'Athletic Facilities'
        PH = 'PH', 'Proximity to Home'

    name = models.CharField(max_length=250)
    position = models.CharField(
        max_length=3,
        choices=Position
    )
    year = models.CharField(
        max_length=2,
        choices=Year,
        default=Year.FR
    )
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    dev = models.CharField(
        max_length=3,
        choices=Dev,
        default=Dev.NRM
    )
    eligibility = models.CharField(
        max_length=3,
        choices=Eligibility,
        default=Eligibility.REC
    )
    interests = MultiSelectField(
        choices=Interests,
        max_choices=3,
        max_length=3
    )
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'recruiting'
        ordering = ['rating']
        indexes = [
            models.Index(fields=['rating', 'position', 'year', 'position'])
        ]

    def __str__(self):
        return f"{self.position} - {self.name} [{self.year}] - {self.rating} OVR"
