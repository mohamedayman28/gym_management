{% extends "base.html" %}
{% block content %}

<h3 class="pt-5">Home page</h3>

<table class="table mb-5">
  <a class="btn btn-success mt-5" href="#" hx-get="{% url 'gym:member_form' %}" hx-target=".member_container"
    hx-swap="outerHTML">
    Add Member
  </a>
  <thead>
    <tr>
      <th scope="col">Member ID</th>
      <th scope="col">Member Name</th>
      <th scope="col">Gender</th>
      <th scope="col">Enrolled date</th>
      <th scope="col">End date</th>
      <th scope="col">Remaining day(s)</th>
    </tr>
  </thead>
  <tbody>
    {% for member in members %}
    <tr>
      <!-- Member ID. -->
      <th scope="row">{{ member.id }}</th>
      <!-- Member name. -->
      <td>{{ member.first_name }} {{ member.last_name }}</td>
      <!-- Gender. -->
      <td>{{ member.get_gender_name }}</td>
      <!-- Enrolled date. -->
      <td>{{ member.enrolled_date }}</td>
      <!-- End date. -->
      <td>{{ member.end_date }}</td>
      <!-- Remaining day(s). -->
      <td class="text-center">{{ member.get_remaining_days }}</td>

      <!-- Update member button. -->
      <td>
        <a href="#" class="text-primary" hx-get="{% url 'gym:member_update' member.pk %}" hx-target=".member_container"
          hx-swap="outerHTML">
          Update
        </a>
      </td>
      <!-- End of update member button. -->

      <!-- Delete member button. -->
      <td>
        <!-- Modal trigger. -->
        <a href="#" class="text-danger" data-toggle="modal" data-target="#member_delete">delete</a>
      </td>
      <!-- Modal structure. -->
      <div class="modal" id="member_delete">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-body"> Delete <b>{{ member.first_name }}</b> Member permanently!!</div>
            <div class="modal-footer">
              <!-- Cancel deletion button. -->
              <button type="button" class="btn btn-primary" data-dismiss="modal">Cancel</button>
              <!-- Confirm deletion button. -->
              <form method="POST" action="{% url 'gym:member_delete' member.id %}">
                {% csrf_token %}
                {{ form }}
                <div class="d-grid">
                  <button class="btn btn-danger" type="submit">
                    Delete
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <!-- End of delete member button. -->
    </tr>
    {% endfor %}
  </tbody>
</table>
{% endblock content %}
