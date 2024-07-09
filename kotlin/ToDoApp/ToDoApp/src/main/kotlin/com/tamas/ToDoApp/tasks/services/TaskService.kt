package com.tamas.ToDoApp.tasks.services

import com.tamas.ToDoApp.tasks.TaskDtoRequest.TaskDtoRequest
import com.tamas.ToDoApp.tasks.TaskDtoRequest.toEntity
import com.tamas.ToDoApp.tasks.TaskDtoResponse.TaskDtoResponse
import com.tamas.ToDoApp.tasks.TaskDtoResponse.toTaskDtoResponse
import com.tamas.ToDoApp.tasks.repository.TaskRepository
import org.springframework.stereotype.Service
import org.springframework.transaction.annotation.Transactional

@Service
class TaskService(var taskRepository: TaskRepository) {

    @Transactional
    fun getTasks(): List<TaskDtoResponse> {
        return taskRepository.findAll().map { it.toTaskDtoResponse() }
    }

    @Transactional
    fun getTaskById(id: Long): TaskDtoResponse? {
        val task = taskRepository.findById(id).orElseThrow { RuntimeException("Task not found") }
        return task.toTaskDtoResponse()
    }

    @Transactional
    fun createTask(taskDto: TaskDtoRequest): TaskDtoResponse {
        val task = taskDto.toEntity()
        taskRepository.save(task)
        return task.toTaskDtoResponse()
    }

    @Transactional
    fun updateTask(taskDto: TaskDtoRequest): Boolean {
        val taskToUpdate = taskRepository.findById(taskDto.id).orElseThrow { RuntimeException("Task not found") }
        taskToUpdate.apply {
            name = taskDto.name
            description = taskDto.description
            status = taskDto.status
            deadline = taskDto.deadline
            userId = taskDto.userId
            updatedAt = taskDto.updatedAt.toString()
        }
        taskRepository.save(taskToUpdate)

        return true
    }

    @Transactional
    fun deleteTask(id: Long) {
        taskRepository.deleteById(id)
    }
}
