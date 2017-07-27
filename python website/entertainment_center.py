import media
import fresh_tomatoes

toy_story=media.Movie("TOY STORY",
                      "A story of a boy and his toys that come to life",
                      "toy_story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar=media.Movie("Avatar",
                   "A marine on an alien planet",
                   "Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
imitation_game=media.Movie("The Imitation Game",
                           "A story of a person who decrypted the enigma",
                           "imitation_game.jpg",
                           "https://www.youtube.com/watch?v=S5CjKEFb-sM")
#imitation_game.show_trailer()

movies=[toy_story,avatar,imitation_game]
fresh_tomatoes.open_movies_page(movies)
