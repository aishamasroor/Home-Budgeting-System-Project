from django.shortcuts import render, redirect
from .models import Category, Transaction
from .forms import CategoryForm, TransactionForm


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def load_form(request):
    form = CategoryForm()
    # form = TransactionForm
    return render(request, 'index.html', {'form': form})


def add(request):
    form = CategoryForm(request.POST)
    form.is_valid()
    form.save()
    return redirect('/categories')


def show_cat(request):
    category = Category.objects.all()  # Instance of Category #
    print(category)
    return render(request, 'showcats.html', {'category': category})


def show(request):
    category = Category.objects.all()  # Instance of Category #
    return render(request, 'show.html', {'category': category})


def edit(request, id):
    category = Category.objects.get(pk=id)
    return render(request, "edit.html", {'category': category})


def update(request, id):
    category = Category.objects.get(pk=id)
    form = CategoryForm(request.POST, instance=category)
    form.save()
    return redirect('/categories')


def delete(request, id):
    category = Transaction.objects.get(pk=id)
    category.delete()
    return redirect('/transpage')

def deletes(request, cat_id):
    category = Category.objects.get(pk=cat_id)
    category.delete()
    return redirect('/categories')

def search(request):
    given_name = request.POST['name']
    category = Category.objects.filter(cat_names__icontains=given_name)
    transaction = Transaction.objects.filter(cat_id__in=category)
    print(transaction)

    return render(request, 'show.html', {'category': category, 'transaction': transaction})


def transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/transpage')
    else:
        cat = Category.objects.order_by('cat_names')
        return render(request, 'transaction.html', {'cat': cat})


def transpage(request):
    trans = Transaction.objects.all()
    return render(request, 'transpage.html', {'trans': trans})


def save(request):
    form = TransactionForm(request.POST)
    form.save()
    return redirect('/transpage')


def showdetails(request):
    cat = Category.objects.order_by('cat_names')
    return render(request, 'showdetails.html', {'cat': cat})


def submit(request):
    sub = Transaction.objects.all()
    return render(request, 'showdetails.html', {'sub': sub})

def show2(request):

    category = Category.objects.order_by('cat_id')
    print(category)
    if request.method == 'GET':
        transactionobj = Transaction.objects.all()
        return render(request, 'show2.html', {'transaction': transactionobj})
    else:
        transactionobj = Transaction.objects.filter(cat_id=request.POST['cat_id'])
        total = 0
        for loop in transactionobj:
            total += loop.amount
        return render(request, 'show2.html', {'transaction': transactionobj, 'total': total})
