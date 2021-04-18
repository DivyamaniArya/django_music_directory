from django.db import models


class Artist(models.Model):
    artist_id = models.AutoField(db_column='ArtistId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artists'


class Album(models.Model):
    album_id = models.AutoField(db_column='AlbumId', primary_key=True)
    title = models.TextField(db_column='Title')
    artist_id = models.ForeignKey(Artist, db_column='ArtistId', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'albums'


class Customer(models.Model):
    customer_id = models.AutoField(db_column='CustomerId', primary_key=True)
    firstname = models.TextField(db_column='FirstName')
    lastname = models.TextField(db_column='LastName')
    company = models.TextField(db_column='Company', blank=True, null=True)
    address = models.TextField(db_column='Address', blank=True, null=True)
    city = models.TextField(db_column='City', blank=True, null=True)
    state = models.TextField(db_column='State', blank=True, null=True)
    country = models.TextField(db_column='Country', blank=True, null=True)
    postal_code = models.TextField(db_column='PostalCode', blank=True, null=True)
    phone = models.TextField(db_column='Phone', blank=True, null=True)
    fax = models.TextField(db_column='Fax', blank=True, null=True)
    email = models.TextField(db_column='Email')
    support_rep_id = models.IntegerField(db_column='SupportRepId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Employee(models.Model):
    employee_id = models.AutoField(db_column='EmployeeId', primary_key=True)
    lastname = models.TextField(db_column='LastName')
    firstname = models.TextField(db_column='FirstName')
    title = models.TextField(db_column='Title', blank=True, null=True)
    reports_to = models.IntegerField(db_column='ReportsTo', blank=True, null=True)
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)
    hire_date = models.DateTimeField(db_column='HireDate', blank=True, null=True)
    address = models.TextField(db_column='Address', blank=True, null=True)
    city = models.TextField(db_column='City', blank=True, null=True)
    state = models.TextField(db_column='State', blank=True, null=True)
    country = models.TextField(db_column='Country', blank=True, null=True)
    postal_code = models.TextField(db_column='PostalCode', blank=True, null=True)
    phone = models.TextField(db_column='Phone', blank=True, null=True)
    fax = models.TextField(db_column='Fax', blank=True, null=True)
    email = models.TextField(db_column='Email', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class Genre(models.Model):
    genre_id = models.AutoField(db_column='GenreId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres'


class Invoice(models.Model):
    invoice_id = models.AutoField(db_column='InvoiceId', primary_key=True)
    customer_id = models.ForeignKey(Customer, db_column='CustomerId', on_delete=models.CASCADE)
    invoice_date = models.DateTimeField(db_column='InvoiceDate')
    billing_address = models.TextField(db_column='BillingAddress', blank=True, null=True)
    billing_city = models.TextField(db_column='BillingCity', blank=True, null=True)
    billing_state = models.TextField(db_column='BillingState', blank=True, null=True)
    billing_country = models.TextField(db_column='BillingCountry', blank=True, null=True)
    billing_postal_code = models.TextField(db_column='BillingPostalCode', blank=True, null=True)
    total = models.TextField(db_column='Total')

    class Meta:
        managed = False
        db_table = 'invoices'


class MediaType(models.Model):
    media_type_id = models.AutoField(db_column='MediaTypeId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media_types'


class Playlist(models.Model):
    playlist_id = models.AutoField(db_column='PlaylistId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playlists'


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)
    idx = models.TextField(blank=True, null=True)
    stat = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'


class Track(models.Model):
    track_id = models.AutoField(db_column='TrackId', primary_key=True)
    name = models.TextField(db_column='Name')
    album_id = models.ForeignKey(Album, db_column='AlbumId', blank=True, null=True, on_delete=models.CASCADE)
    media_type_id = models.ForeignKey(MediaType, db_column='MediaTypeId', on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, db_column='GenreId', blank=True, null=True, on_delete=models.CASCADE)
    composer = models.TextField(db_column='Composer', blank=True, null=True)
    milliseconds = models.IntegerField(db_column='Milliseconds')
    bytes = models.IntegerField(db_column='Bytes', blank=True, null=True)
    unit_price = models.TextField(db_column='UnitPrice')

    class Meta:
        managed = False
        db_table = 'tracks'


class PlaylistTrack(models.Model):
    playlist_id = models.ForeignKey(Playlist, db_column='PlaylistId', on_delete=models.CASCADE)
    track_id = models.ForeignKey(Track, db_column='TrackId', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'playlist_track'


class InvoiceItem(models.Model):
    invoice_line_id = models.AutoField(db_column='InvoiceLineId', primary_key=True)
    invoice_id = models.IntegerField(db_column='InvoiceId')
    track_id = models.ForeignKey(Track, db_column='TrackId', on_delete=models.CASCADE)
    unit_price = models.TextField(db_column='UnitPrice')
    quantity = models.IntegerField(db_column='Quantity')

    class Meta:
        managed = False
        db_table = 'invoice_items'
