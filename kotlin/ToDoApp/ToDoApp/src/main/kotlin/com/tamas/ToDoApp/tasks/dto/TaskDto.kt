package com.tamas.ToDoApp.tasks.dto

import com.tamas.ToDoApp.tasks.domain.Status
import com.tamas.ToDoApp.tasks.domain.TaskEntity

data class TaskDto(
    val id: Long,
    val name: String,
    val description: String?,
    val status: Status,
    val deadline: String?,
    val userId: Long,
    val updatedAt: String,
    val createdAt: String
)

fun TaskEntity.toDto() = TaskDto(
    id = this.id,
    name = this.name,
    description = this.description,
    status = this.status,
    deadline = this.deadline.toString(),
    userId = this.userId,
    createdAt = this.createdAt.toString(),
    updatedAt = this.updatedAt.toString()
)

fun TaskDto.toEntity() = TaskEntity(
    id = this.id,
    name = this.name,
    description = this.description,
    status = this.status,
    deadline = this.deadline,
    userId = this.userId,
    createdAt = this.createdAt,
    updatedAt = this.updatedAt
)