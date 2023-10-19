import { NgModule, isDevMode } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { ServiceWorkerModule } from '@angular/service-worker';
import { WebcamModule } from 'ngx-webcam';
import { FitComponentComponent } from './fit-component/fit-component.component';
import { FaceComponentComponent } from './face-component/face-component.component';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    FitComponentComponent,
    FaceComponentComponent
  ],
  imports: [
    WebcamModule,
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    ServiceWorkerModule.register('ngsw-worker.js', {
      enabled: !isDevMode(),
      // Register the ServiceWorker as soon as the application is stable
      // or after 30 seconds (whichever comes first).
      registrationStrategy: 'registerWhenStable:30000'
    })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
