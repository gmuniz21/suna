"use client"

import { useEffect, useState } from "react"
import { SidebarLeft } from "@/components/sidebar/sidebar-left"
import {
  SidebarInset,
  SidebarProvider,
} from "@/components/ui/sidebar"
import { MaintenanceAlert } from "@/components/maintenance-alert"

interface DashboardLayoutProps {
  children: React.ReactNode
}

export default function DashboardLayout({
  children,
}: DashboardLayoutProps) {
  const [showMaintenanceAlert, setShowMaintenanceAlert] = useState(false)
  
  useEffect(() => {
    // Show the maintenance alert when component mounts
    setShowMaintenanceAlert(true)
  }, [])

  return (
    <SidebarProvider>
      <SidebarLeft />
      <SidebarInset>
        <div className="bg-background">
          {children}
        </div>
      </SidebarInset>
      
      <MaintenanceAlert 
        open={showMaintenanceAlert} 
        onOpenChange={setShowMaintenanceAlert}
        closeable={true}
      />
    </SidebarProvider>
  )
} 