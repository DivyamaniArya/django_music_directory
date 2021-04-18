from rest_framework.generics import DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.filters import SearchFilter
from django.db.models import Q
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema

from .models import (Track, Artist, Album, Customer, Employee,
                     Genre, Invoice, MediaType, Playlist, InvoiceItem)
from .serializers import (TrackSerializer, TrackUpdateSerializer, ArtistSerializer,
                          AlbumSerializer, CustomerSerializer, EmployeeSerializer,
                          GenreSerializer, InvoiceSerializer, MediaTypeSerializer,
                          PlaylistSerializer, InvoiceItemSerializer)


class TrackListView(ListAPIView):
    http_method_names = ['get']
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["name", "composer", "genre_id__name"]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_queryset(self):
        search_query = self.request.query_params.get('search')
        if search_query:
            return Track.objects.filter(Q(name__icontains=search_query)
                                        | Q(genre_id__name__icontains=search_query)
                                        | Q(composer__icontains=search_query))
        else:
            return Track.objects.all()

    query_param = openapi.Parameter(
        "search",
        openapi.IN_QUERY,
        description="search query param",
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(manual_parameters=[query_param], tags=["Track"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TrackUpdateView(UpdateAPIView):
    http_method_names = ['post']
    serializer_class = TrackUpdateSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        track_id = self.kwargs.get('track_id', None)
        return Track.objects.get(pk=track_id)

    @swagger_auto_schema(tags=["Track"])
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class TrackDetailsView(RetrieveAPIView):
    http_method_names = ['get']
    serializer_class = TrackSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        track_id = self.kwargs.get('track_id', None)
        return Track.objects.get(pk=track_id)

    @swagger_auto_schema(tags=["Track"])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TrackDestroyView(DestroyAPIView):
    http_method_names = ['delete']
    serializer_class = TrackSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        track_id = self.kwargs.get('track_id', None)
        return Track.objects.get(pk=track_id)

    @swagger_auto_schema(tags=["Track"])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ArtistListView(ListAPIView):
    http_method_names = ['get']
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    @swagger_auto_schema(tags=["Artist"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ArtistUpdateView(UpdateAPIView):
    http_method_names = ['post']
    serializer_class = ArtistSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        artist_id = self.kwargs.get('artist_id', None)
        return Artist.objects.get(pk=artist_id)

    @swagger_auto_schema(tags=["Artist"])
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ArtistDetailsView(RetrieveAPIView):
    http_method_names = ['get']
    serializer_class = ArtistSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        artist_id = self.kwargs.get('artist_id', None)
        return Artist.objects.get(pk=artist_id)

    @swagger_auto_schema(tags=["Artist"])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ArtistDestroyView(DestroyAPIView):
    http_method_names = ['delete']
    serializer_class = ArtistSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        artist_id = self.kwargs.get('artist_id', None)
        return Artist.objects.get(pk=artist_id)

    @swagger_auto_schema(tags=["Artist"])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AlbumListView(ListAPIView):
    http_method_names = ['get']
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    @swagger_auto_schema(tags=["Album"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AlbumUpdateView(UpdateAPIView):
    http_method_names = ['post']
    serializer_class = AlbumSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        album_id = self.kwargs.get('album_id', None)
        return Album.objects.get(pk=album_id)

    @swagger_auto_schema(tags=["Album"])
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class AlbumDetailsView(RetrieveAPIView):
    http_method_names = ['get']
    serializer_class = AlbumSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        album_id = self.kwargs.get('album_id', None)
        return Album.objects.get(pk=album_id)

    @swagger_auto_schema(tags=["Album"])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class AlbumDestroyView(DestroyAPIView):
    http_method_names = ['delete']
    serializer_class = AlbumSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        album_id = self.kwargs.get('album_id', None)
        return Album.objects.get(pk=album_id)

    @swagger_auto_schema(tags=["Album"])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CustomerListView(ListAPIView):
    http_method_names = ['get']
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    @swagger_auto_schema(tags=["Customer"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CustomerUpdateView(UpdateAPIView):
    http_method_names = ['post']
    serializer_class = CustomerSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        customer_id = self.kwargs.get('customer_id', None)
        return Customer.objects.get(pk=customer_id)

    @swagger_auto_schema(tags=["Customer"])
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CustomerDetailsView(RetrieveAPIView):
    http_method_names = ['get']
    serializer_class = CustomerSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        customer_id = self.kwargs.get('customer_id', None)
        return Customer.objects.get(pk=customer_id)

    @swagger_auto_schema(tags=["Customer"])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CustomerDestroyView(DestroyAPIView):
    http_method_names = ['delete']
    serializer_class = CustomerSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        customer_id = self.kwargs.get('customer_id', None)
        return Customer.objects.get(pk=customer_id)

    @swagger_auto_schema(tags=["Customer"])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class EmployeeListView(ListAPIView):
    http_method_names = ['get']
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    @swagger_auto_schema(tags=["Employee"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EmployeeUpdateView(UpdateAPIView):
    http_method_names = ['post']
    serializer_class = EmployeeSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        employee_id = self.kwargs.get('employee_id', None)
        return Employee.objects.get(pk=employee_id)

    @swagger_auto_schema(tags=["Employee"])
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class EmployeeDetailsView(RetrieveAPIView):
    http_method_names = ['get']
    serializer_class = EmployeeSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        employee_id = self.kwargs.get('employee_id', None)
        return Employee.objects.get(pk=employee_id)

    @swagger_auto_schema(tags=["Employee"])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class EmployeeDestroyView(DestroyAPIView):
    http_method_names = ['delete']
    serializer_class = EmployeeSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        employee_id = self.kwargs.get('employee_id', None)
        return Employee.objects.get(pk=employee_id)

    @swagger_auto_schema(tags=["Employee"])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GenreListView(ListAPIView):
    http_method_names = ['get']
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    @swagger_auto_schema(tags=["Genre"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GenreUpdateView(UpdateAPIView):
    http_method_names = ['post']
    serializer_class = GenreSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        genre_id = self.kwargs.get('genre_id', None)
        return Genre.objects.get(pk=genre_id)

    @swagger_auto_schema(tags=["Genre"])
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class GenreDetailsView(RetrieveAPIView):
    http_method_names = ['get']
    serializer_class = GenreSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        genre_id = self.kwargs.get('genre_id', None)
        return Genre.objects.get(pk=genre_id)

    @swagger_auto_schema(tags=["Genre"])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GenreDestroyView(DestroyAPIView):
    http_method_names = ['delete']
    serializer_class = GenreSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        genre_id = self.kwargs.get('genre_id', None)
        return Genre.objects.get(pk=genre_id)

    @swagger_auto_schema(tags=["Genre"])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class InvoiceListView(ListAPIView):
    http_method_names = ['get']
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    @swagger_auto_schema(tags=["Invoice"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class InvoiceUpdateView(UpdateAPIView):
    http_method_names = ['post']
    serializer_class = InvoiceSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        invoice_id = self.kwargs.get('invoice_id', None)
        return Invoice.objects.get(pk=invoice_id)

    @swagger_auto_schema(tags=["Invoice"])
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class InvoiceDetailsView(RetrieveAPIView):
    http_method_names = ['get']
    serializer_class = InvoiceSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        invoice_id = self.kwargs.get('invoice_id', None)
        return Invoice.objects.get(pk=invoice_id)

    @swagger_auto_schema(tags=["Invoice"])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class InvoiceDestroyView(DestroyAPIView):
    http_method_names = ['delete']
    serializer_class = InvoiceSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        invoice_id = self.kwargs.get('invoice_id', None)
        return Invoice.objects.get(pk=invoice_id)

    @swagger_auto_schema(tags=["Invoice"])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MediaTypeListView(ListAPIView):
    http_method_names = ['get']
    serializer_class = MediaTypeSerializer
    queryset = MediaType.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    @swagger_auto_schema(tags=["MediaType"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MediaTypeUpdateView(UpdateAPIView):
    http_method_names = ['post']
    serializer_class = MediaTypeSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        media_type_id = self.kwargs.get('media_type_id', None)
        return MediaType.objects.get(pk=media_type_id)

    @swagger_auto_schema(tags=["MediaType"])
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class MediaTypeDetailsView(RetrieveAPIView):
    http_method_names = ['get']
    serializer_class = MediaTypeSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        media_type_id = self.kwargs.get('media_type_id', None)
        return MediaType.objects.get(pk=media_type_id)

    @swagger_auto_schema(tags=["MediaType"])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MediaTypeDestroyView(DestroyAPIView):
    http_method_names = ['delete']
    serializer_class = MediaTypeSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        media_type_id = self.kwargs.get('media_type_id', None)
        return MediaType.objects.get(pk=media_type_id)

    @swagger_auto_schema(tags=["MediaType"])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PlaylistListView(ListAPIView):
    http_method_names = ['get']
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    @swagger_auto_schema(tags=["Playlist"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PlaylistUpdateView(UpdateAPIView):
    http_method_names = ['post']
    serializer_class = PlaylistSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        playlist_id = self.kwargs.get('playlist_id', None)
        return Playlist.objects.get(pk=playlist_id)

    @swagger_auto_schema(tags=["Playlist"])
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class PlaylistDetailsView(RetrieveAPIView):
    http_method_names = ['get']
    serializer_class = PlaylistSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        playlist_id = self.kwargs.get('playlist_id', None)
        return Playlist.objects.get(pk=playlist_id)

    @swagger_auto_schema(tags=["Playlist"])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PlaylistDestroyView(DestroyAPIView):
    http_method_names = ['delete']
    serializer_class = PlaylistSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        playlist_id = self.kwargs.get('playlist_id', None)
        return Playlist.objects.get(pk=playlist_id)

    @swagger_auto_schema(tags=["Playlist"])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class InvoiceItemListView(ListAPIView):
    http_method_names = ['get']
    serializer_class = InvoiceItemSerializer
    queryset = InvoiceItem.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    @swagger_auto_schema(tags=["InvoiceItem"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class InvoiceItemUpdateView(UpdateAPIView):
    http_method_names = ['post']
    serializer_class = InvoiceItemSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        invoice_line_id = self.kwargs.get('invoice_line_id', None)
        return InvoiceItem.objects.get(pk=invoice_line_id)

    @swagger_auto_schema(tags=["InvoiceItem"])
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class InvoiceItemDetailsView(RetrieveAPIView):
    http_method_names = ['get']
    serializer_class = InvoiceItemSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        invoice_line_id = self.kwargs.get('invoice_line_id', None)
        return InvoiceItem.objects.get(pk=invoice_line_id)

    @swagger_auto_schema(tags=["InvoiceItem"])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class InvoiceItemDestroyView(DestroyAPIView):
    http_method_names = ['delete']
    serializer_class = InvoiceItemSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_object(self):
        invoice_line_id = self.kwargs.get('invoice_line_id', None)
        return InvoiceItem.objects.get(pk=invoice_line_id)

    @swagger_auto_schema(tags=["InvoiceItem"])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
