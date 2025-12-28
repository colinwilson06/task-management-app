from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.task_service import (
    service_get_all_tasks,
    service_create_task,
    service_update_task,
    service_delete_task
)

task_bp = Blueprint("task_bp", __name__)

@task_bp.route("/tasks", methods=["GET"])
@jwt_required()
def get_all_tasks():
    data = service_get_all_tasks()
    return jsonify(data), 200

@task_bp.route("/tasks", methods=["POST"])
@jwt_required()
def create_new_task():
    data = request.json
    task_id = service_create_task(data)
    return jsonify({"message": "Task created", "id": task_id}), 201

@task_bp.route("/tasks/<int:id>", methods=["PUT"])
@jwt_required()
def update_existing(id):
    data = request.json
    service_update_task(id, data)
    return jsonify({"message": "Task updated"}), 200

@task_bp.route("/tasks/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_existing(id):
    service_delete_task(id)
    return jsonify({"message": "Task deleted"}), 200
