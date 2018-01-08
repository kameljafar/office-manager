from graphene_django.types import ObjectType
from graphene_django_extras import DjangoFilterPaginateListField

from apps.employees import models
from apps.employees.schema import mutation
from apps.employees.schema import types

__all__ = [
    'EmployeeQuery', 'EmployeeMutation'
]


class EmployeeQuery(ObjectType):
    positions = DjangoFilterPaginateListField(types.PositionType)
    specializations = DjangoFilterPaginateListField(types.SpecializationType)
    employees = DjangoFilterPaginateListField(types.EmployeeType)

    class Meta:
        abstract = True

    def resolve_specializations(self, info):
        return models.Specialization.objects.all()

    def resolve_positions(self, info):
        return models.Position.objects.all()

    def resolve_employees(self, info):
        return models.Employee.objects.all()


class EmployeeMutation(ObjectType):
    position_create = mutation.ModelPositionMutation.CreateField()
    position_update = mutation.ModelPositionMutation.UpdateField()
    position_delete = mutation.ModelPositionMutation.DeleteField()

    specialization_create = mutation.ModelSpecializationMutation.CreateField()
    specialization_update = mutation.ModelSpecializationMutation.UpdateField()
    specialization_delete = mutation.ModelSpecializationMutation.DeleteField()

    employee_create = mutation.ModelEmployeeMutation.get_mutation_field(
        'create_mutation'
    )
    employee_update = mutation.ModelEmployeeMutation.UpdateField()
    employee_delete = mutation.ModelEmployeeMutation.DeleteField()

    change_password = mutation.ModelEmployeeMutation.get_mutation_field(
        'password_mutation'
    )

    change_current_employee = mutation.ModelEmployeeMutation.get_mutation_field(
        'current_employee_mutation'
    )

    class Meta:
        abstract = True
