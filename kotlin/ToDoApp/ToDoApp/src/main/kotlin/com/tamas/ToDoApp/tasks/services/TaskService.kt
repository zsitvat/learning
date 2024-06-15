package com.tamas.ToDoApp.modules.tasks.services

import com.tamas.ToDoApp.modules.tasks.dto.TaskDto
import org.springframework.stereotype.Service
import com.tamas.ToDoApp.modules.tasks.repository.TaskRepository

@Service
class TaskService(var taskRepository: TaskRepository) {

    fun getTasks(): List<TaskDto> {
        val tasks = taskRepository.findAll().toList()
        return tasks
    }

    fun getTaskById(id: Long): TaskDto {
        val task = taskRepository.findById(id).get()
        return task
    }

    fun postTask(task: TaskDto) {
        db.save(task)
    }

fun updateTask(id: Long, task: TaskDto) {
        val taskToUpdate = taskRepository.findById(id).get()
        taskToUpdate.name = task.name
        taskToUpdate.description = task.description
        taskToUpdate.status = task.status
        taskToUpdate.deadline = task.deadline
        taskToUpdate.userId = task.userId
        taskToUpdate.updatedAt = task.updatedAt
        taskToUpdate.createdAt = task.createdAt
        db.save(taskToUpdate)
    }
}


