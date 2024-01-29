import datetime
from django.views import generic
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import redirect, render

from .models import Reservation, Room, Booked
from .forms import SearchForm, ReserveForm


class IndexView(generic.edit.FormView):
    template_name = 'hotel/index.html'
    form_class = SearchForm


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            checkin: datetime.date = form.cleaned_data["checkin"]
            checkout: datetime.date = form.cleaned_data["checkout"]
            headcount = form.cleaned_data["headcount"]

        days = (checkout - checkin).days
        dates = []

        for i in range(days):
            dates.append(checkin + datetime.timedelta(i))

        twn_remain = []
        dbl_remain = []
        sgl_remain = []

        twn_rooms = Room.objects.filter(room_type='twn').count()
        dbl_rooms = Room.objects.filter(room_type='dbl').count()
        sgl_rooms = Room.objects.filter(room_type='sgl').count()

        for date in dates:
            booked_rooms = Booked.objects.filter(date=date).values()
            if booked_rooms.exists():
                twn_remain.append(twn_rooms - booked_rooms[0]['twin_booked'])
                dbl_remain.append(dbl_rooms - booked_rooms[0]['double_booked'])
                sgl_remain.append(sgl_rooms - booked_rooms[0]['single_booked'])
            else:
                twn_remain.append(twn_rooms)
                dbl_remain.append(dbl_rooms)
                sgl_remain.append(sgl_rooms)

        availability = [min(twn_remain), min(dbl_remain), min(sgl_remain)]

        form = SearchForm()
        checkin_date = checkin.strftime('%Y/%m/%d')
        checkout_date = checkout.strftime('%Y/%m/%d')
        ctx = {"form": form, "checkin_date": checkin_date, \
               "checkout_date": checkout_date, "availability": availability}

        return render(request, 'hotel/search.html', ctx)

    else:
        form = SearchForm()
    ctx = {"form": form}
    return render(request, 'hotel/search.html', ctx)


def reserve(request):
    if request.method == "POST":
        # When the "予約" button is clicked with data filled on the search page
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        room_type = request.POST['room_type']

        '''
        form = ReserveForm({'checkin': checkin_formated,
                            'checkout': checkout_formated,
                            'room_type': room_type })'''
        form = ReserveForm()

        ctx = {'form': form, 'checkin': checkin, 'checkout': checkout,
               'room_type': room_type}

        return render(request, 'hotel/reserve.html', ctx)

    else:
        return redirect('hotel:search')


def confirm(request):
    if request.method == "POST":
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        room_type = request.POST['room_type']

        form = ReserveForm(request.POST)
        if form.is_valid():
            headcount = form.cleaned_data['headcount']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
                
        ctx = { 'checkin': checkin, 'checkout': checkout,
                'room_type': room_type, 'headcount': headcount,
                'name': name, 'email': email }

        return render(request, 'hotel/confirm.html', ctx)

    else:
        return redirect('hotel:search')


def book(request):
    if request.method == "POST":
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        room_type = request.POST['room_type']
        if room_type == 'ツイン':
            room_type_name = 'twn'
        elif room_type == 'ダブル':
            room_type_name = 'dbl'
        else:
            room_type_name = 'sgl'

        format = '%Y/%m/%d'
        checkin_date = datetime.datetime.strptime(checkin, format)
        checkout_date = datetime.datetime.strptime(checkout, format)
        
        headcount = request.POST['headcount']
        name = request.POST['name']
        email = request.POST['email']

        reservation = Reservation(checkin=checkin_date, checkout=checkout_date,
                                  headcount=headcount, name=name, email=email,
                                  room_type=room_type_name)
        reservation.save()

        for i in range((checkout_date-checkin_date).days):
            date = checkin_date + datetime.timedelta(i)
            try:
                booked = Booked.objects.get(date=date)
            except Booked.DoesNotExist:
                if room_type == 'ツイン':
                    new = Booked(date=date, twin_booked=1)
                elif room_type == 'ダブル':
                    new = Booked(date=date, double_booked=1)
                else:
                    new = Booked(date=date, single_booked=1)
                new.save()
            else:
                if room_type == 'ツイン':
                    booked.twin_booked += 1
                elif room_type == 'ダブル':
                    booked.double_booked += 1
                else:
                    booked.single_booked += 1
                booked.save()

        '''return render(request, 'hotel/thanks.html')'''
        return redirect('hotel:thanks')

    else:
        return redirect('hotel:index')


def thanks(request):
    return render(request, 'hotel/thanks.html')
