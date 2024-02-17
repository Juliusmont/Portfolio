from datetime import datetime

class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

class Task:
    def __init__(self, id, description, duration, importance, urgency, deadline, monetary_cost, completion_percentage, status, user_id, task_type):
        self.id = id
        self.description = description
        self.duration = duration
        self.importance = importance
        self.urgency = urgency
        self.deadline = deadline
        self.monetary_cost = monetary_cost
        self.completion_percentage = completion_percentage
        self.status = status
        self.user_id = user_id
        self.task_type = task_type
    
    def Cloturer(self):
        self.completion_status = "réalisé"

class TachePonctuelle(Task):
    def Cloturer(self):
        super().Cloturer()
        # 

class TacheRecurrente(Task):
    def __init__(self, name, duration, importance, urgency, deadline, monetary_value, initial_completion, completion_status, end_date):
        super().__init__(name, duration, importance, urgency, deadline, monetary_value, initial_completion, completion_status)
        self.end_date = end_date

    def Cloturer(self):
        super().Cloturer()
        # 

class Calendar:
    def __init__(self, deadline):
        self.deadline = deadline
        self.tasks = []

    def Alerter(self):
        # Implémentez la logique d'alerte si nécessaire
        pass

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def calculate_weight(self, task):
        # Implémentez la logique de calcul du poids d'une tâche
        pass

    def classify_task(self, task):
        # Implémentez la logique de classification d'une tâche
        pass

    def plan_task(self, task, date):
        # Implémentez la logique de planification d'une tâche
        pass

class Quadrant:
    def __init__(self, nom):
        self.nom = nom
        self.tasks = []

    def RealiserAction(self):
        # Implémentez la logique pour réaliser une action dans le quadrant
        pass