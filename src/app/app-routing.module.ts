import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FaceComponentComponent } from './face-component/face-component.component';
import { FitComponentComponent } from './fit-component/fit-component.component';

const routes: Routes = [
  {path: 'faceauth', component: FaceComponentComponent},
  {path: 'fitnesstracker', component: FitComponentComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
