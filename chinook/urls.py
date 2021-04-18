from django.urls import include, path

from .views import *

track_urlpatterns = [
    path('.list', TrackListView.as_view(), name='track-list'),
    path('.update/<int:track_id>/', TrackUpdateView.as_view(), name='track-update'),
    path('.delete/<int:track_id>/', TrackDestroyView.as_view(), name='track-destroy'),
    path('.details/<int:track_id>/', TrackDetailsView.as_view(), name='track-details'),
]

artist_urlpatterns = [
    path('.list', ArtistListView.as_view(), name='artist-list'),
    path('.update/<int:artist_id>/', ArtistUpdateView.as_view(), name='artist-update'),
    path('.delete/<int:artist_id>/', ArtistDestroyView.as_view(), name='artist-destroy'),
    path('.details/<int:artist_id>/', ArtistDetailsView.as_view(), name='artist-details'),
]

album_urlpatterns = [
    path('.list', AlbumListView.as_view(), name='album-list'),
    path('.update/<int:album_id>/', AlbumUpdateView.as_view(), name='album-update'),
    path('.delete/<int:album_id>/', AlbumDestroyView.as_view(), name='album-destroy'),
    path('.details/<int:album_id>/', AlbumDetailsView.as_view(), name='album-details'),
]

customer_urlpatterns = [
    path('.list', CustomerListView.as_view(), name='customer-list'),
    path('.update/<int:customer_id>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('.delete/<int:customer_id>/', CustomerDestroyView.as_view(), name='customer-destroy'),
    path('.details/<int:customer_id>/', CustomerDetailsView.as_view(), name='customer-details'),
]

employee_urlpatterns = [
    path('.list', EmployeeListView.as_view(), name='employee-list'),
    path('.update/<int:employee_id>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('.delete/<int:employee_id>/', EmployeeDestroyView.as_view(), name='employee-destroy'),
    path('.details/<int:employee_id>/', EmployeeDetailsView.as_view(), name='employee-details'),
]

genre_urlpatterns = [
    path('.list', GenreListView.as_view(), name='genre-list'),
    path('.update/<int:genre_id>/', GenreUpdateView.as_view(), name='genre-update'),
    path('.delete/<int:genre_id>/', GenreDestroyView.as_view(), name='genre-destroy'),
    path('.details/<int:genre_id>/', GenreDetailsView.as_view(), name='genre-details'),
]

invoice_urlpatterns = [
    path('.list', InvoiceListView.as_view(), name='invoice-list'),
    path('.update/<int:invoice_id>/', InvoiceUpdateView.as_view(), name='invoice-update'),
    path('.delete/<int:invoice_id>/', InvoiceDestroyView.as_view(), name='invoice-destroy'),
    path('.details/<int:invoice_id>/', InvoiceDetailsView.as_view(), name='invoice-details'),
]

media_type_urlpatterns = [
    path('.list', MediaTypeListView.as_view(), name='media_type-list'),
    path('.update/<int:media_type_id>/', MediaTypeUpdateView.as_view(), name='media_type-update'),
    path('.delete/<int:media_type_id>/', MediaTypeDestroyView.as_view(), name='media_type-destroy'),
    path('.details/<int:media_type_id>/', MediaTypeDetailsView.as_view(), name='media_type-details'),
]

playlist_urlpatterns = [
    path('.list', PlaylistListView.as_view(), name='playlist-list'),
    path('.update/<int:playlist_id>/', PlaylistUpdateView.as_view(), name='playlist-update'),
    path('.delete/<int:playlist_id>/', PlaylistDestroyView.as_view(), name='playlist-destroy'),
    path('.details/<int:playlist_id>/', PlaylistDetailsView.as_view(), name='playlist-details'),
]

invoice_item_urlpatterns = [
    path('.list', InvoiceItemListView.as_view(), name='invoice_item-list'),
    path('.update/<int:invoice_item_id>/', InvoiceItemUpdateView.as_view(), name='invoice_item-update'),
    path('.delete/<int:invoice_item_id>/', InvoiceItemDestroyView.as_view(), name='invoice_item-destroy'),
    path('.details/<int:invoice_item_id>/', InvoiceItemDetailsView.as_view(), name='invoice_item-details'),
]

urlpatterns = [
    path("track", include(track_urlpatterns)),
    path("artist", include(artist_urlpatterns)),
    path("album", include(album_urlpatterns)),
    path("customer", include(customer_urlpatterns)),
    path("employee", include(employee_urlpatterns)),
    path("genre", include(genre_urlpatterns)),
    path("invoice", include(invoice_urlpatterns)),
    path("invoice_item", include(invoice_item_urlpatterns)),
    path("media_type", include(media_type_urlpatterns)),
    path("playlist", include(playlist_urlpatterns)),
]
