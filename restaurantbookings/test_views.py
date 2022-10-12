""" Automated testing for the views.py file """
from django.test import TestCase
from django.contrib.auth.models import User
from restaurantbookings.models import Booking, Contact


class TestGuestViews(TestCase):
    """ Test that the views.py file render the templates
    and context correctly for guest users """

    def setUp(self):
        """ Create instances of booking and contact objects
        that can be used in the other tests """

        test_user = User.objects.create_user(
            username="ck",
            password="dpReporter"
        )

        Booking.objects.create(
            guest=test_user,
            table=2,
            people=2,
            booking_date_time_start="2022-10-13 12:53:00+00:00",
            booking_date_time_end="2022-10-13 13:53:00+00:00",
        )

    def log_in(self):
        """ This is to help test the views
        that require a user to be logged in
        to access """
        self.client.login(
            username="ck",
            password="dpReporter"
        )

    def test_home_view_get(self):
        """ Test home view renders correctly """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_menu_view_get(self):
        """ Test menu page renders correctly """
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html', 'base.html')

    def test_booking_view(self):
        """ Test that availability booking form renders correctly """
        self.log_in()
        response = self.client.get('/restaurantbookings/book/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'availability_form.html',
                                'base.html')

    def test_user_bookings_view(self):
        """ Test view for users to see a list of their bookings """
        # page requires user to be logged in
        self.log_in()
        response = self.client.get('/restaurantbookings/my_bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_bookings.html', 'base.html')

    def test_edit_booking_view(self):
        """ Test view for users to edit their bookings """
        # page requires user to be logged in
        self.log_in()
        response = self.client.get('/restaurantbookings/editbooking/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_booking.html', 'base.html')

    def confirm_delete_view(self):
        """ Test view for users to edit their bookings """
        # page requires user to be logged in
        self.log_in()
        response = self.client.get('/restaurantbookings/confirmdelete/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_delete.html', 'base.html')


class TestSuperViews(TestCase):
    """ Test that the views.py file render the templates
    and context correctly for superusers """

    def setUp(self):
        """ Create instances of booking and contact objects
        that can be used in the other tests """

        test_superuser = User.objects.create_superuser(
            username="ck",
            password="dpReporter"
        )

        Booking.objects.create(
            guest=test_superuser,
            table=2,
            people=2,
            booking_date_time_start="2022-10-13 12:53:00+00:00",
            booking_date_time_end="2022-10-13 13:53:00+00:00",
        )

        Contact.objects.create(
            first_name="Clark",
            last_name="Kent",
            contact_number='012345678910',
            email_address='clark.kent@dailyplanet.net',
            message='test message content',
            created_on="2022-10-13 13:53:00+00:00"
        )

    def log_in(self):
        """ This is to help test the views
        that require a user to be logged in
        to access """
        self.client.login(
            username="ck",
            password="dpReporter"
        )

    def test_home_view_get(self):
        """ Test home view renders correctly """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_menu_view_get(self):
        """ Test menu page renders correctly """
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html', 'base.html')

    def test_booking_view(self):
        """ Test that availability booking form renders correctly """
        self.log_in()
        response = self.client.get('/restaurantbookings/book/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'availability_form.html',
                                'base.html')

    def test_admin_dashoard(self):
        """ Test view for admin to view list of bookings and messages """
        # page requires user to be logged in
        self.log_in()
        response = self.client.get('/admindashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_dashboard.html', 'base.html')

    def test_edit_booking_view(self):
        """ Test view for users to edit their bookings """
        # page requires user to be logged in
        self.log_in()
        response = self.client.get('/restaurantbookings/editbooking/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_booking.html', 'base.html')

    def confirm_delete_view(self):
        """ Test view for users to edit their bookings """
        # page requires user to be logged in
        self.log_in()
        response = self.client.get('/restaurantbookings/confirmdelete/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_delete.html', 'base.html')

    def confirm_clear_message_view(self):
        """ Test view for users to edit their bookings """
        # page requires user to be logged in
        self.log_in()
        response = self.client.get('/clearmessage/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_clear_message.html',
                                'base.html')
