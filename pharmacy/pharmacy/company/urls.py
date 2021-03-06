from django.urls import include, path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^(?P<pharmacy_id>\d+)/add_stock_user/(?P<username>.*)/$', add_stock_user),
    url(r'^(?P<pharmacy_id>\d+)/add_stock/$', add_stock),
    url(r'^(?P<pharmacy_id>\d+)/get_stocks/$', get_stocks),
    url(r'^(?P<stock_id>\d+)/add_stock_item/$', add_stock_item),
    url(r'^(?P<stock_id>\d+)/add_stock_item_user/$', add_stock_item_user),
    url(r'^(?P<stock_id>\d+)/get_stock_items/$', get_stock_items),
    url(r'^(?P<stock_id>\d+)/get_stock_items_user/$', get_stock_items_user),
    url(r'^(?P<stock_id>\d+)/get_total_stock_items/$', get_total_stock_items),
    url(r'^(?P<stock_id>\d+)/get_total_stock_items_user/$', get_total_stock_items_user),
    url(r'^(?P<stock_id>\d+)/edit_stock/$', edit_stock),
    url(r'^(?P<stock_item_id>\d+)/edit_stock_item/$', edit_stock_item),
    url(r'^(?P<stock_id>\d+)/delete_stock/$', delete_stock),
    url(r'^(?P<stock_item_id>\d+)/delete_stock_item/$', delete_stock_item),
    url(r'^(?P<stock_id>\d+)/add_company/$', add_company),
    url(r'^(?P<stock_id>\d+)/add_order_user/(?P<username>.*)/$', add_order_by_user),
    url(r'^(?P<order_id>\d+)/delete_order/$', delete_order),
    url(r'^(?P<order_id>\d+)/delete_order_user/$', delete_order_user),
    url(r'^(?P<order_id>\d+)/fulfil_order/$', fulfil_order_user),
    url('get_order_user/(?P<username>.*)/$', get_order_by_user),
    url('get_user_orders/$', get_user_orders),
    url(r'^(?P<stock_id>\d+)/add_order/$', add_order),
    url('get_companys/$', get_companys),
    url('get_orders/$', get_orders),
    url(r'^(?P<company_id>\d+)/get_orders_by_company/$', get_orders_by_company),
    url('add_companys/$', add_company_total),
    url(r'^(?P<company_id>\d+)/edit_company/$', edit_company),
    url(r'^(?P<company_id>\d+)/delete_company/$', delete_company),
    url('get_message/admin/help/$', get_chat_users),
    url('get_message/(?P<username>.*)/$', get_message),
    url('add_message/(?P<username>.*)/$', add_message),
]
