import os

filepath = r"c:\Users\a\Desktop\procourse\venv\course\templates\detail.html"
with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_content = """            <!-- Lessons Grid section -->
            <div class="row g-4">
              {% for l in lesson %}
              <div class="col-md-6 mb-4">
                <div class="card h-100 shadow border-0" style="border-radius: 15px; transition: transform 0.3s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                  <div class="card-body p-4">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                      <span class="badge" style="background-color: var(--accent-color, #ffc451); color: #151515; font-size: 0.85rem; padding: 0.5em 0.8em; border-radius: 8px;">{{ l.get_day_display }}</span>
                      <span class="text-muted small"><i class="bi bi-clock me-1"></i>{{ l.time|time:"g:i A" }}</span>
                    </div>
                    <h5 class="card-title fw-bold mb-3 text-dark" style="font-size: 1.25rem;">{{ l.course_name.name|default:l.course_name }}</h5>
                    <p class="card-text text-muted" style="line-height: 1.6;">{{ l.description|truncatewords:18 }}</p>
                  </div>
                  <div class="card-footer bg-transparent border-top-0 p-4 pt-0 text-center">
                    <button class="btn btn-outline-dark rounded-pill w-100 fw-semibold" style="border-color: #151515; transition: all 0.3s ease;">View Lesson</button>
                  </div>
                </div>
              </div>
              {% empty %}
              <div class="col-12 text-center py-5">
                <div class="text-muted"><i class="bi bi-exclamation-circle fs-1 d-block mb-3"></i>No lessons found for this course.</div>
              </div>
              {% endfor %}
            </div>
"""

out = []
in_article = False
for i, line in enumerate(lines):
    if "<article class=\"article\">" in line:
        in_article = True
        out.append(new_content)
    if not in_article:
        out.append(line)
    if "</article>" in line:
        in_article = False

with open(filepath, "w", encoding="utf-8") as f:
    f.writelines(out)
