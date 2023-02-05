from django.db import migrations

def create_example_dso(apps, schema_editor):
    DSO = apps.get_model("EnergyProvider", "DSO")
    enel = DSO(name="Enel", availability=True, price=0.50)
    dsoA = DSO(name="DSOA", availability=True, price=0.40)
    dsoB = DSO(name="DSOB", availability=True, price=0.35)
    dsoC = DSO(name="DSOC", availability=True, price=0.60)
    dsoD = DSO(name="DSOD", availability=False, price=0.70)
    dsoE = DSO(name="DSOE", availability=False, price=0.80)
    enel.save()
    dsoA.save()
    dsoB.save()
    dsoC.save()
    dsoD.save()
    dsoE.save()

class Migration(migrations.Migration):

    dependencies = [
        ('EnergyProvider', '0005_remove_dso_station'),
    ]

    operations = [
        migrations.RunPython(create_example_dso)
    ]