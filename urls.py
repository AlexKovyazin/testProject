from views import Index, RegionCities

routes = {
    '/': Index(),
    '/get_regions/': RegionCities()
}
