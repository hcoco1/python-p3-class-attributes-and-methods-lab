class Song:

    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    count = 0 # Class attribute to keep track of the number of new songs

    def __init__(self, name, artist, genre):
        Song.add_to_genres(genre)  # Call class method to add genre
        Song.add_to_artists(artist)  # Call class method to add artist
        Song.add_song_to_count()  # Call class method to increment count
        Song.add_to_genre_count(genre)  # Call class method to update genre count
        Song.add_to_artist_count(artist)  # Call class method to update artist count
        self.name = name
        self.artist = artist
        self.genre = genre 
        
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1  # Increment the count when a new song is created
           
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)  # Add unique genre to the list
            
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)  # Add unique artist to the list

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1  # Update genre count
        
    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1  # Update artist count
        
        
    @classmethod
    def create_histogram(cls):
        genre_histogram = {}
        for genre in cls.genres:
            genre_histogram[genre] = cls.genre_count.get(genre, 0)

        artist_histogram = {}
        for artist in cls.artists:
            artist_histogram[artist] = cls.artist_count.get(artist, 0)

        return genre_histogram, artist_histogram