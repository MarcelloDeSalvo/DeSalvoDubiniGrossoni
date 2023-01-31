from django.db import migrations
def create_example_sockets(apps, schema_editor):
    Socket = apps.get_model("Socket", "Socket")
    station = apps.get_model("ChargingStation", "ChargingStation")

    sock = Socket(chargingStation=station.objects.get(pk=1), type='F', status='Y', price=0.15)
    sock.save()
    sock = Socket(chargingStation=station.objects.get(pk=1), type='F', status='Y', price=0.15)
    sock.save()
    sock = Socket(chargingStation=station.objects.get(pk=1), type='R', status='Y', price=0.13)
    sock.save()
    sock = Socket(chargingStation=station.objects.get(pk=1), type='R', status='Y', price=0.13)
    sock.save()
    sock = Socket(chargingStation=station.objects.get(pk=1), type='S', status='Y', price=0.11)
    sock.save()

    sock = Socket(chargingStation=station.objects.get(pk=2), type='F', status='Y', price=0.6)
    sock.save()
    sock = Socket(chargingStation=station.objects.get(pk=2), type='F', status='Y', price=0.6)
    sock.save()
    sock = Socket(chargingStation=station.objects.get(pk=2), type='R', status='Y', price=0.52)
    sock.save()
    sock = Socket(chargingStation=station.objects.get(pk=2), type='R', status='N', price=0.52)
    sock.save()
    sock = Socket(chargingStation=station.objects.get(pk=2), type='S', status='N', price=0.44)
    sock.save()

    sock = Socket(chargingStation=station.objects.get(pk=3), type='F', status='Y', price=1.2)
    sock.save()
    sock = Socket(chargingStation=station.objects.get(pk=3), type='F', status='Y', price=1.2)
    sock.save()
    sock = Socket(chargingStation=station.objects.get(pk=3), type='R', status='Y', price=1.04)
    sock.save()
    sock = Socket(chargingStation=station.objects.get(pk=3), type='R', status='N', price=1.04)
    sock.save()


    

class Migration(migrations.Migration):

    dependencies = [
        ('Socket', '0003_rename_socketstatus_socket_status_and_more'),
        ('ChargingStation', '0017_stations_example'),
        ('EnergyProvider', '0008_merge_0006_dso_example_0007_battery_example')
    ]

    operations = [
        migrations.RunPython(create_example_sockets)
    ]