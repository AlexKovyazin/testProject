from views import Index, RegionCities, DownloadUsersXlsx

routes = {
    '/': Index(),
    '/get_regions/': RegionCities(),
    '/download_users_xlsx/': DownloadUsersXlsx(),
}
