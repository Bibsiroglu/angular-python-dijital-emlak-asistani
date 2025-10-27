// src/main.ts
import { bootstrapApplication } from '@angular/platform-browser';
// Doğru isim AppComponent olmalı
import { AppComponent } from './app/app'; // VEYA './app/app';

import { appConfig } from './app/app.config';

bootstrapApplication(AppComponent, appConfig) // KRİTİK: AppComponent kullanıldığından emin olun
  .catch((err) => console.error(err));