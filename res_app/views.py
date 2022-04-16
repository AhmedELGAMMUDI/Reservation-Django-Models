from django.views.generic.list import ListView
from res_app.models import Reservation
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

class ReservationListView(ListView):
    model = Reservation
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ReservationListView, self).get_context_data(**kwargs) 
        list_reservation = Reservation.objects.all()
        paginator = Paginator(list_reservation, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            reservation_list = paginator.page(page)
        except PageNotAnInteger:
            reservation_list = paginator.page(1)
        except EmptyPage:
            reservation_list = paginator.page(paginator.num_pages)
            
        context['reservation_list'] = reservation_list
        return context

