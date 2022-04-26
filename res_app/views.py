from django.views.generic.list import ListView
from res_app.models import Reservation
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import OuterRef, Subquery


class ReservationListView(ListView):
    model = Reservation
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ReservationListView, self).get_context_data(**kwargs) 
        list_reservation = Reservation.objects.annotate(previous_reservation = Subquery(
                                Reservation.objects.filter(
                                    rental=OuterRef('rental'),checkin__lt=OuterRef('checkin')
                                )
                                .order_by("-checkin")[:1]
                                .values('id')
                            )).select_related("rental")    
        context['reservation_list'] = list_reservation
        return context

