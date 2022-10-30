from star import Star

def create_stars(screen, stars):
    star = Star(screen)
    star_width = star.rect.width
    star_height = star.rect.height
    available_space_x = (star.screen_rect.width / (star_width * 2))
    number_stars_x = int(available_space_x / star_width)
    available_space_y = (star.screen_rect.height / (star_height * 2))
    number_stars_y = int(available_space_y / star_height)

    for row_num in range(number_stars_y):
        for star_num in range(number_stars_x):
            star = Star(screen)
            star.x = star.rect.width + 2 * star.rect.width * star_num
            star.rect.x = star.x
            star.rect.y = star.rect.height + 2 * star.rect.height * star_num
            stars.add(star)