import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MenuItemSupplierHomeComponent } from './home/MenuItemSupplier-home.component';
import { MenuItemSupplierNewComponent } from './new/MenuItemSupplier-new.component';
import { MenuItemSupplierDetailComponent } from './detail/MenuItemSupplier-detail.component';

const routes: Routes = [
  {path: '', component: MenuItemSupplierHomeComponent},
  { path: 'new', component: MenuItemSupplierNewComponent },
  { path: ':id', component: MenuItemSupplierDetailComponent,
    data: {
      oPermission: {
        permissionId: 'MenuItemSupplier-detail-permissions'
      }
    }
  }
];

export const MENUITEMSUPPLIER_MODULE_DECLARATIONS = [
    MenuItemSupplierHomeComponent,
    MenuItemSupplierNewComponent,
    MenuItemSupplierDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MenuItemSupplierRoutingModule { }