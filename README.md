# ml_examples
В проекте содержатся примеры решения задач:


- House Prices - Advanced Regression Techniques
- Titanic - Machine Learning from Disaster


Для данных с Титаника есть api /survival, в который можно передать признаки и получить предсказание.

Для запуска api:
~~~
flask --app app run
~~~

Запрос будет доступен по адресу localhost:5000/survival

Пример запроса:

```json
{
  "Pclass": 1,
  "Sex": 2,
  "Age":  18.0,
  "Fare": 1.28,
  "is_alone": 1,
  "Embarked_Q": false,
  "Embarked_S": false 
}
```

