package com.tamas.ToDoApp.tasks.services

import com.tamas.ToDoApp.tasks.domain.TaskEntity
import com.tamas.ToDoApp.tasks.dto.TaskDto
import com.tamas.ToDoApp.tasks.repository.TaskRepository
import org.springframework.stereotype.Service
import org.springframework.transaction.annotation.Transactional
import com.tamas.ToDoApp.tasks.domain.Status
import com.tamas.ToDoApp.tasks.dto.toDto
import com.tamas.ToDoApp.tasks.dto.toEntity

@Service
class TaskService(private val taskRepository: TaskRepository) {

    fun getTasks(): List<TaskDto> {
        return taskRepository.findAll().map { it.toDto() }
    }

    fun getTaskById(id: Long): TaskDto {
        val task = taskRepository.findById(id).orElseThrow { RuntimeException("Task not found") }
        return task.toDto()
    }

    @Transactional
    fun postTask(taskDto: TaskDto) {
        val task = taskDto.toEntity()
        taskRepository.save(task)
    }

    @Transactional
    fun updateTask(id: Long, taskDto: TaskDto) {
        val taskToUpdate = taskRepository.findById(id).orElseThrow { RuntimeException("Task not found") }
        taskToUpdate.apply {
            name = taskDto.name
            description = taskDto.description
            status = taskDto.status
            deadline = taskDto.deadline
            userId = taskDto.userId
            updatedAt = taskDto.updatedAt
        }
        taskRepository.save(taskToUpdate)
    }
}
