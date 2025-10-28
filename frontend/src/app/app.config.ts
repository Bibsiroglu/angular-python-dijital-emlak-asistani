// src/app/app.config.ts

import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http'; // API iletişimleri için KRİTİK

import { routes } from './app.routes'; 

export const appConfig: ApplicationConfig = { // 'config' yerine 'appConfig' olarak isimlendirelim.
  providers: [
    provideRouter(routes), 
    provideHttpClient() 
  ]
};