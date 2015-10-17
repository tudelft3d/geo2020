---
layout: page
title: Theses in progress
permalink: /inprogress/
---

 <table class="striped bordered responsive-table">
  <thead>
    <tr>
        <th data-field="id">Surname</th>
        <th data-field="name">Name</th>
        <th data-field="price">Title</th>
        <th data-field="price">Start</th>
        <th data-field="price">Mentor #1</th>
        <th data-field="price">Mentor #2</th>
    </tr>
  </thead>
  <tbody>
  {% assign students = site.data.students_current | sort: 'surname' %}
  {% for i in students %}
    <tr>
      <td>{{ i.surname }}</td>
      <td>{{ i.name }}</td>
      <td>{{ i.title }}</td>
      <td>{{ i.start }}</td>
      <td>{{ i.mentor1 }}</td>
      <td>{{ i.mentor2 }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>