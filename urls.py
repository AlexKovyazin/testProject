from views import Index, RegionCities, DownloadUsersXlsx, DownloadUsersPdf

routes = {
    '/': Index(),
    '/get_regions/': RegionCities(),
    '/download_users_xlsx/': DownloadUsersXlsx(),
    '/download_users_pdf/': DownloadUsersPdf(),
}
