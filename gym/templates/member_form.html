{% extends 'base.html' %}
{% load static %}

{% comment %}
This template is related to:
* MemberFormView
* MemberUpdateView
{% endcomment %}

{% load static %}

{% block content %}
  <div class="text-danger p-4">
    <p>{{ form.non_field_errors }}</p>
  </div>

{% with request.resolver_match as match %}
  {% if match.url_name == 'member_update' %}
    <h3 class="pb-4">Update Member</h3>
    <form method="POST" action="{% url 'gym:member_update' form.instance.pk %}">
  {% else %}
      <h3 class="pb-4">Add Member</h3>
      <form method="POST" action="{% url 'gym:member_form' %}">
  {% endif %}
    {% csrf_token %}
{% endwith %}

    <!-- Row for: user field. -->
    <div class="row">
      <!-- User field. -->
      <div class="col-auto">
        <!-- Label. -->
        <label class="mr-sm-2" for="{{ form.user.id_for_label }}">{{ form.user.label }}</label>
        <!-- Input. -->
        <select class="custom-select mr-sm-2" id="{{ form.user.id_for_label }}" style="cursor: pointer" name="user">
          {% for choice in form.user %}
          {{ choice }}
          {% endfor %}
        </select>
        <!-- Error messages. -->
        <small class=" form-text text-danger">{{ form.user.errors }}</small>
      </div>
    </div>
    <!-- End of row for: user field. -->

    <hr>

    <!-- Row for: first name, last name and gender fields. -->
    <div class="row">
      <!-- First name field. -->
      <div class="col-auto">
        <!-- Label. -->
        <label for="{{ form.first_name.id_for_label }}">{{ form.first_name.label }}</label>
        <!-- Input. -->
        <input class="form-control" id="{{ form.first_name.id_for_label }}" placeholder="{{ form.first_name.label }}"
          name="first_name" value="{% if form.first_name.value %}{{ form.first_name.value }}{% endif %}">
        <!-- Error messages. -->
        <small class="form-text text-danger">{{ form.last_name.errors }}</small>
      </div>
      <!-- End of first name field. -->
      <!-- Last name field. -->
      <div class="col-auto">
        <!-- Label. -->
        <label for="{{ form.last_name.id_for_label }}">{{ form.last_name.label }}</label>
        <!-- Input. -->
        <input class="form-control" id="{{ form.last_name.id_for_label }}" placeholder="{{ form.last_name.label }}"
          name="last_name" value="{% if form.last_name.value %}{{ form.last_name.value }}{% endif %}">
        <!-- Error messages. -->
        <small class="form-text text-danger">{{ form.last_name.errors }}</small>
      </div>
      <!-- End of last name field. -->
      <!-- Gender field. -->
      <div class="col-auto">
        <!-- Label. -->
        <label class="mr-sm-2" for="{{ form.gender.id_for_label }}">{{ form.gender.label }}</label>
        <!-- Input. -->
        <select class="custom-select mr-sm-2" id="{{ form.gender.id_for_label }}" style="cursor: pointer" name="gender">
          <option selected>...</option>
          {% for choice in form.gender %}
          {{ choice }}
          {% endfor %}
        </select>
        <!-- Error messages. -->
        <small class="form-text text-danger">{{ form.gender.errors }}</small>
      </div>
      <!-- End of gender field. -->
    </div>
    <!-- End of row for: first name, last name and gender fields. -->

    <hr>

    <!-- Row for: enrolled field and end date fields. -->
    <div class="row">
      <!-- Enrolled date field. -->
      <div class="col-auto">
        <!-- Label. -->
        <label for="{{ form.enrolled_date.id_for_label }}">{{ form.enrolled_date.label }}</label>
        <!-- Input. -->
        <input class="form-control" id="{{ form.enrolled_date.id_for_label }}"
          placeholder="{{ form.enrolled_date.label }}" name="enrolled_date" type="date" style="cursor: pointer"
          value="{% if form.enrolled_date.value %}{{ form.enrolled_date.value|date:" Y-m-d" }}{% endif %}">
        <!-- Error messages. -->
        <small class="form-text text-danger">{{ form.enrolled_date.errors }}</small>
      </div>
      <!-- End of enrolled date field. -->
      <!-- End date field. -->
      <div class="col-auto">
        <!-- Label. -->
        <label for="{{ form.end_date.id_for_label }}">{{ form.end_date.label }}</label>
        <!-- Input. -->
        <input class="form-control" id="{{ form.end_date.id_for_label }}" placeholder="{{ form.end_date.label }}"
          name="end_date" type="date" style="cursor: pointer"
          value="{% if form.end_date.value %}{{ form.end_date.value|date:" Y-m-d" }}{% endif %}">
        <!-- Error messages. -->
        <small class="form-text text-danger">{{ form.end_date.errors }}</small>
      </div>
      <!-- End of end date field. -->
    </div>
    <!-- End of row for: enrolled field and end date fields. -->

    <hr>

    <!-- Submit button. -->
    <div class="d-grid">
      {% with request.resolver_match as match %}
      {% if match.url_name == "member_update" %}
      <button class="btn btn-primary">Update</button>
      {% else%}
      <button class="btn btn-primary">Add</button>
      {% endif %}
      {% endwith %}
      <button class="btn btn-secondary" hx-get="{% url 'gym:index' %}" hx-target=".member_container"
        hx-swap="outerHTML">
        Cancel
      </button>
    </div>
  </form>
  <!-- End of contact form. -->
{% endblock content %}
