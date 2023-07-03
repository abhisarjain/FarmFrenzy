from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import auth
from .models import Buyer, Crop, Negotiation, Seller,Order
from .forms import CropForm
# Create your views here.
def homepage(request):
    return render(request,'index.html')

def registerasbuyer(request):

     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        mail = request.POST['email']
       
        
        User = get_user_model()
        if not User.objects.filter(username=username).exists():
            ins = User.objects.create_user(username=username, password=password, first_name=fn, last_name=ln,
                                           email=mail,is_seller=False)
            ins.save()
            return  redirect('/login')
        else:
            return render(request, 'register.html')
     else:

        return render(request,'register.html')
     


def registerasseller(request):

     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        mail = request.POST['email']
       
        
        User = get_user_model()
        if not User.objects.filter(username=username).exists():
            ins = User.objects.create_user(username=username, password=password, first_name=fn, last_name=ln,
                                           email=mail,is_seller=True)
            ins.save()
            return redirect('/login')
        else:
            return render(request, 'register.html')
     else:

        return render(request,'register.html')
     return render(request,'register.html')
    

def login(request):
        if request.method == 'POST':
            username = request.POST['usernamelg']
            password = request.POST['passwordlg']
            User = get_user_model()

           
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
               
                return render(request, 'login.html')

        else:
            
            return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



def mycrops(request):
    if request.user.is_authenticated:
        crops = Crop.objects.filter(seller=request.user)
        context = {'crops': crops}

        if request.method == 'POST':
            
            cropname = request.POST.get('cropname')
            cropvariety = request.POST.get('cropvariety')
            croptype = request.POST.get('croptype')
            ppkg = request.POST.get('ppkg')
            shelflife = request.POST.get('shelflife')
            quant = request.POST.get('quant')
            desc = request.POST.get('desc')

            crop = Crop(seller = request.user,
            name=cropname,
            variety=cropvariety,
            type=croptype,
            price_per_kg=ppkg,
            shelf_life=shelflife,
            quantity=quant,
            description=desc
            )
            crop.save()
            return redirect('/mycrops')

        return render(request, 'mycrops.html', context)
    else:
        return redirect('/login')
    

def crops(request):
    if(request.user.is_seller):
        return redirect('/mycrops')
    crop = Crop.objects.all()
    context = {'crops': crop}
    return render(request,'crops.html',context)


def readmore(request, id):

    crops = Crop.objects.filter(id=id)
    crop_get = Crop.objects.get(id=id)

    context = {'crops': crops}
  

    if request.method == 'POST':
        quant  = int(request.POST['quantity'])
        delcrops = Crop.objects.filter(id=id)
        buyer = Buyer.objects.get(user = request.user)
        order = Order(buyer=buyer,crop=crop_get,quantity_bought=quant,price=crop_get.price_per_kg)
        order.save()
        for delcrop in delcrops:
            
            delcrop.quantity = delcrop.quantity - quant
            delcrop.save()
        return redirect('/myorders')

    return render(request, 'readmore.html',context)


def deletecrop(request,id):
    crops = Crop.objects.filter(id=id)
    crops.delete()
    return redirect('/mycrops')

def editcrop(request,id):
    crop = Crop.objects.get(id=id)
    form = CropForm(request.POST or None,instance=crop)
    if form.is_valid():
        form.save()
        return redirect('/mycrops')
    context = {'form': form}
    return render(request,'editcrops.html',context)


def negotiate(request,id):
    if request.method == 'POST':
        pp = request.POST['pp']
        quant = request.POST['quant']
        desc = request.POST['desc']
        crop = Crop.objects.get(id=id)
        buyer = Buyer.objects.get(user=request.user)
        seller = Seller.objects.get(user=crop.seller)
        neg = Negotiation(buyer=buyer,proposed_price=pp,crop=crop,seller=seller,desc=desc,quantity=quant)
        neg.save()
        return redirect('/buyernegotiations')
    return render(request,'negotiate.html')


def sellernegotiations(request):
    seller = Seller.objects.get(user=request.user)
    neg = Negotiation.objects.filter(seller=seller)
    return render(request,'sellernegotiations.html',{'negs': neg})



def accept(request,id):
    if request.method == 'POST':
        Negotiation.objects.filter(pk=id).update(accepted=True)
        Negotiation.objects.filter(pk=id).update(awaited=False)
       
        return redirect('/sellernegotiations')
    return render(request,'sellernegotiations.html')


def reject(request,id):
    if request.method == 'POST':
        Negotiation.objects.filter(pk=id).update(rejected=True)
        Negotiation.objects.filter(pk=id).update(awaited=False)
       
        return redirect('/sellernegotiations')
    return render(request,'sellernegotiations.html')


def buyernegotiations(request):
    buyer = Buyer.objects.get(user=request.user)
    neg = Negotiation.objects.filter(buyer=buyer)
    return render(request,'buyernegotiations.html',{'negs': neg})


def buynow(request,id):
    if request.method == 'POST':
        neg = Negotiation.objects.get(id=id)
        crops = Crop.objects.filter(id=neg.crop.id)
        for crop in crops:
            
            crop.quantity = crop.quantity - neg.quantity
            crop.save()
        Negotiation.objects.filter(id=id).update(bought=True)
        return redirect('/buyernegotiations')
    return render(request,'buyernegotiations.html')



def myorders(request):
    buyer = Buyer.objects.get(user=request.user)
    orders = Order.objects.filter(buyer=buyer)
    context = {'orders':orders}
    return render(request,'myorders.html',context)



def about(request):
    return render(request,'about.html')