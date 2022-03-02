{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
  <title>Gym</title>
  <link rel="stylesheet" href="{% static 'css/stylesheet.css' %}">
</head>

<body>
  <!-- NOTE: member_container used as Htmx DOM class. -->
  <div class="member_container">
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
      <div class="container">
        <!-- Title. -->
        <a class="navbar-brand" href="#" hx-get="{% url 'gym:index' %}" hx-target=".member_container"
          hx-swap="outerHTML">
          Gym Management
        </a>
        <!-- Home page link. -->
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="#" hx-get="{% url 'gym:index' %}" hx-target=".member_container"
              hx-swap="outerHTML">
              Home
            </a>
          </li>
          <!-- Add new member link. -->
          <li class="nav-item">
            <a class="nav-link" href="#" hx-get="{% url 'gym:member_form' %}" hx-target=".member_container"
              hx-swap="outerHTML">
              Add Member
            </a>
          </li>
          <!-- Logout link. -->
          {% if user.is_authenticated %}
          <li class="nav-item">
            <a class="nav-link" href="{% url 'gym:logout' %}">
              Logout</a>
          </li>
          {% else %}
          <!-- Login -->
          <li class="nav-item">
            <a class="nav-link" href="#" hx-get="{% url 'gym:login' %}" hx-target=".member_container"
              hx-swap="outerHTML">
              Login
            </a>
          </li>
          {% endif %}
          <!-- Admin link. -->
          {% if user.is_superuser %}
          <li class="nav-item">
            <a class="nav-link" target="_blank" href="{% url 'admin:index' %}">Admin</a>
          </li>
          {% endif %}
        </ul>
        <!-- Search form. -->
        <form class="form-inline mt-2 mt-md-0">
          <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </nav>
    <!-- Django jinja block. -->
    <div class="container">
      {% block content %}{% endblock content %}
    </div>
  </div>

  <!-- Bootstrap core JSs-->
  <!-- NOTE: Bootstrap JSs files order is important -->
  <script src="{% static 'js/jquery.js' %}"></script>
  <script src="{% static 'js/popper.js' %}"></script>
  <script src="{% static 'js/bootstrap.js' %}"></script>
  <!-- Htmx JS-->
  <script src="{% static 'js/htmx.js' %}"></script>
  <!-- Django CSRF token on POST -->
  <script>
    document.body.addEventListener('htmx:configRequest', (event) => {
      event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
    })
  </script>
</body>

</html>
