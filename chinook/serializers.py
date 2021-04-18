from rest_framework.serializers import ModelSerializer

from .models import Track, Artist, Album, Customer, Employee, Genre, Invoice, MediaType, Playlist, InvoiceItem


class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class TrackUpdateSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = ['name', 'composer']


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class MediaTypeSerializer(ModelSerializer):
    class Meta:
        model = MediaType
        fields = '__all__'


class PlaylistSerializer(ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'


class InvoiceItemSerializer(ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'
