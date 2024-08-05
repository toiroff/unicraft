document.addEventListener('DOMContentLoaded', function () {
  const testSelect = document.getElementById('id_test');
  const subTestContainer = document.getElementById('subTestContainer');
  const subTestsDiv = document.getElementById('subTests');

  testSelect.addEventListener('change', function () {
      const selectedTestId = this.value;
      if (selectedTestId) {
          fetch(`/get_sub_tests/${selectedTestId}/`)
              .then(response => response.json())
              .then(data => {
                  subTestsDiv.innerHTML = '';
                  data.sub_tests.forEach(sub_test => {
                      const subTestLabel = document.createElement('label');
                      subTestLabel.textContent = `${sub_test.name} (max ${sub_test.max_score}): `;
                      const subTestInput = document.createElement('input');
                      subTestInput.type = 'number';
                      subTestInput.name = `sub_test_${sub_test.id}`;
                      subTestInput.max = sub_test.max_score;
                      subTestInput.min = 0;
                      subTestInput.required = true;
                      subTestsDiv.appendChild(subTestLabel);
                      subTestsDiv.appendChild(subTestInput);
                      subTestsDiv.appendChild(document.createElement('br'));
                  });
                  subTestContainer.style.display = 'block';
              });
      } else {
          subTestContainer.style.display = 'none';
      }
  });
});
