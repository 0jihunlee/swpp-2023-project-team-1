package com.project.spire.network.auth

import com.project.spire.network.auth.request.EmailRequest
import com.project.spire.network.auth.request.LoginRequest
import com.project.spire.network.auth.request.RefreshRequest
import com.project.spire.network.auth.request.RegisterRequest
import com.project.spire.network.auth.request.VerifyCodeRequest
import com.project.spire.network.auth.response.LoginSuccess
import com.project.spire.network.auth.response.RefreshSuccess
import com.project.spire.network.auth.response.RegisterSuccess
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.Header
import retrofit2.http.POST


interface AuthAPI {
    @POST("auth/login")
    suspend fun login(@Body loginRequest: LoginRequest): Response<LoginSuccess>

    @GET("auth/logout")
    suspend fun logout(@Header("Authorization") token: String): Response<Void>

    @POST("auth/refresh")
    suspend fun refresh(@Body refreshRequest: RefreshRequest): Response<RefreshSuccess>

    @POST("auth/register")
    suspend fun register(@Body registerRequest: RegisterRequest): Response<RegisterSuccess>

    @POST("auth/email")
    suspend fun email(@Body emailRequest: EmailRequest): Response<Void>

    @POST("auth/verify/code")
    suspend fun verifyCode(@Body verifyCodeRequest: VerifyCodeRequest): Response<Void>

//    @GET("auth/check")
//    suspend fun check(@Body checkRequest: CheckRequest): Response<CheckSuccess>
}