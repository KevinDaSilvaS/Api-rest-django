from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'size_page'
    max_page_size = 10
