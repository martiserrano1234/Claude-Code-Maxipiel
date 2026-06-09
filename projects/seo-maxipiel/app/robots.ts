import type { MetadataRoute } from "next";

export const dynamic = "force-static";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: { userAgent: "*", allow: "/" },
    sitemap: "https://guia.maxipiel.com.mx/sitemap.xml",
    host: "https://guia.maxipiel.com.mx",
  };
}
