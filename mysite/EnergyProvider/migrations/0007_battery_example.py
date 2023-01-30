from django.db import migrations

def create_example_battery(apps, schema_editor):
    BSS = apps.get_model("EnergyProvider", "BSS")
    station = apps.get_model("ChargingStation", "ChargingStation")

    bss1 = BSS(name="BSS_A", availability=True, price=0.10, isActive=True, station=station.objects.get(pk=1), capacity=100, currentEnergy=100)
    bss1.save()

    bss2 = BSS(name="BSS_B", availability=True, price=0.20, isActive=False, station=station.objects.get(pk=2), capacity=100, currentEnergy=50)
    bss2.save()

    bss3 = BSS(name="BSS_C", availability=True, price=0.80, isActive=True, station=station.objects.get(pk=3), capacity=100, currentEnergy=20)
    bss3.save()
    

class Migration(migrations.Migration):

    dependencies = [
        ('ChargingStation', '0017_stations_example'),
    ]

    operations = [
        migrations.RunPython(create_example_battery)
    ]