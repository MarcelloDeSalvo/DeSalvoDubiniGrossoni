from django.db import migrations

def create_example_stations(apps, schema_editor):
    Station = apps.get_model("ChargingStation", "ChargingStation")
    s1 = Station(city="Milan", address="Via Milano, 1", active_dso_id=1)
    s1.save()
    s1.connected_dsos.set([1,2])

    s2 = Station(city="Milan", address="Via Milano, 2", active_dso_id=2)
    s2.save()
    s2.connected_dsos.set([2,3,4])

    s3 = Station(city="Milan", address="Piazza Leonardo da Vinci, 32", active_dso_id=1)
    s3.save()
    s3.connected_dsos.set([1,2,5,6])



class Migration(migrations.Migration):

    dependencies = [
        ('ChargingStation', '0016_chargingstation_city'),
        ('EnergyProvider', '0006_dso_example')
    ]

    operations = [
        migrations.RunPython(create_example_stations)
    ]