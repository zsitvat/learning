package com.tamas.ToDoApp.tasks.repository

import com.tamas.ToDoApp.tasks.domain.TaskEntity
import org.springframework.data.jpa.repository.JpaRepository
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;

interface TaskRepository : JpaRepository<TaskEntity, Long>, JpaSpecificationExecutor<TaskEntity>