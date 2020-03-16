from fonctionnements.models import Infobule



def get_infobules(request):
    infobules = Infobule.objects.all().values()

    return {"infobules": infobules}