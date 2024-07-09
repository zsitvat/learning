package com.tamas.ToDoApp

import com.tamas.ToDoApp.tasks.TaskDtoRequest.TaskDtoRequest
import com.tamas.ToDoApp.tasks.TaskDtoResponse.TaskDtoResponse
import com.tamas.ToDoApp.tasks.domain.Status
import org.junit.jupiter.api.Assertions.assertTrue
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.boot.test.web.client.TestRestTemplate
import org.junit.jupiter.api.Test


@SpringBootTest(
    webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT
)

class TaskDTOTest(@Autowired var restTemplate: TestRestTemplate) {
    private final val taskDTORequest = TaskDtoRequest(
        id = 1,
        name = "Task",
        description = "description",
        status = Status.TODO,
        deadline = "2024.01.01",
        userId = 1,
        updatedAt = "2024.01.01",
        createdAt = "2024.01.01"
    )

    @Test
    fun testTaskCreation() {
        val result = this.restTemplate.postForEntity("/tasks/create", taskDTORequest, TaskDtoResponse::class.java)
        assertTrue { result.body?.name.equals("Task") }
        assertTrue { result.body?.description.equals("description") }
        assertTrue { result.body?.status?.equals(Status.TODO) ?: false }
        assertTrue { result.body?.deadline.equals("2024.01.01") }
        assertTrue { result.body?.userId?.equals(1) == true }
        assertTrue { result.body?.updatedAt.equals("2024.01.01") }
        assertTrue { result.body?.createdAt.equals("2024.01.01") }
    }

    @Test
    fun testTaskUpdate() {
        val result = this.restTemplate.postForEntity("/tasks/update", taskDTORequest, Boolean::class.java)
        assertTrue { result.body == true }
    }
}